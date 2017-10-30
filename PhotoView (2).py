import httplib, urllib, base64, json
from PIL import Image
from MongoDbConn import recordDetection
import os, os.path


# Replace the subscription_key string value with your valid subscription key.
subscription_key = '1c3eaf5241ef4ad3bc25c8326d929fd2'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    #'Content-Type': 'application/json',
	'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})


def analyzeImage( Image ):

	# The URL of a JPEG image to analyze.
	#body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"
	body = open(Image, "rb").read()

	try:
		# Execute the REST API call and get the response.
		conn = httplib.HTTPSConnection("westcentralus.api.cognitive.microsoft.com")
		conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
		response = conn.getresponse()
		data = response.read()

		# 'data' contains the JSON data. The following formats the JSON data for display.
		parsed = json.loads(data)
		#print ("Response:")
		#print (json.dumps(parsed, sort_keys=True, indent=2))
		conn.close()

	except Exception as e:
		print('Error:')
		print(e)
	return parsed
	
imgs = []
path = "C:\SWLAB\Python\Images"
valid_images = [".jpg",".gif",".png",".tga"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(os.path.join(path,f))
for img in imgs :
	print img
	#curr=Image.open(img)
	#curr.show()
	response=analyzeImage(img)
	
	#print json.dumps(response)
	#print 'Keys in temp :',response.keys()
	#count the tags back fromMicrosoft API
	nr_tags=len(response['description']['tags'])
	recordDetection(response);
	for idxtag in range(nr_tags):
		print response['description']['tags'][idxtag]
		if response['description']['tags'][idxtag] == 'man': print "alarm set what are you doing"
			
			
	