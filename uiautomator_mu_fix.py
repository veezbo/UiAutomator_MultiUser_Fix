import os, re, sys
from pyparsing import Keyword, nestedExpr, Suppress

dir = ""

#Ensure that we are in the correct directory
if re.search(".*/AOSP$", os.getcwd()):
	dir = "AOSP"
elif re.search(".*/adt-bundle-[^/]*$", os.getcwd()):
	dir = "SDK"
else:
	print "Please Enter either the adt-bundle (released SDK) or AOSP (open source) directory"
	sys.exit(1)


#Give the user a chance to quit if they haven't backed up the file yet
print "Please Ensure that You've Backed up either:"
print "    adt-bundle-<version>/sdk/sources/android-<api_level>/com/android/server/accessibility/AccessibilityManagerService.java class in the released SDK"
print "    frameworks/base/services/java/com/android/server/accessibility/AccessibilityManagerService.java class in AOSP"
print "Do you still wish to continue? enter y/n, and press enter"


#If yes..
if raw_input() == "y":

	#Read in API Level if in SDK
	api = -1
	if dir == "SDK":
		print "Please Enter the API level you want to change: "
		api = int(raw_input())


	#Open the correct file and save to a string
	FILE = ""
	if dir == "SDK":
		FILE = "sdk/sources/android-" + str(api) + "/com/android/server/accessibility/AccessibilityManagerService.java"
	elif dir == "AOSP":
		FILE = "frameworks/base/services/java/com/android/server/accessibility/AccessibilityManagerService.java"

	FILE_STRING = open(FILE, "rb").read()


	#Generate the grammar for the security checks that must be removed
	excludeUserSecurity = Keyword('if (resolvedUserId != mCurrentUserId)') + nestedExpr(opener='{', closer='}')
	

	#Remove all instances of substrings that match the grammar (via Suppress)
	OUT_STRING = Suppress(excludeUserSecurity).transformString(FILE_STRING)


	#Write out to a temp file first
	OUT_FILE = FILE + ".temp"
	open(OUT_FILE, "wb").write(OUT_STRING)

	#Rename the file to the original file for in-place editing
	os.rename(OUT_FILE, FILE)

else:
	print "Exiting.."
	sys.exit(1)