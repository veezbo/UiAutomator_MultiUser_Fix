Multi-User UiAutomator Fix
=========================

    UPDATED 9/4/13

Fixes the problem UiAutomator currently has with multiple users in the Android Open Source Project.

The prior fix that relied on the uiautomator_fix.py script is no longer necessary. It is recommended to avoid using this method entirely (as it may have side effects), but the instructions for doing so are included at the end of this README.

The current fix identifies the problem, and fixes that problem directly in a way that will not have side effects on other applications.

For more information, see the [bug report] [1]
and the [AOSP Patch] [2] I submitted (currently in the reviewing process)
	
	[1]: http://code.google.com/p/android/issues/detail?id=58987 "Bug Report"
	[2]: https://android-review.googlesource.com/64730 "AOSP Patch"

Instructions
------------

In the repo, I've included my locally-built uiautomator.jar files with the fix applied (built for generic, maguro, and manta). Pick the one you need and see if it works for you. Also, I think you'll want to rename the .jar file back to uiautomator.jar before doing anything with it.

Otherwise, follow these steps for downloading and applying the fix to AOSP:

1. Initialize your environment here: http://source.android.com/source/initializing.html
2. Download the source: http://source.android.com/source/downloading.html#initializing-a-repo-client  (I would recommend running repo sync -j#, where # is at least the number of cores you have on your computer).
3. You'll then want to modify the Launcher.java file as I have in the bug fix.
4. Then, you'll need to build it: http://source.android.com/source/building-running.html  (alternatively, you can use the script under my Android_Scripts repo called build.sh).
5. Finally, you need to flash your device: http://source.android.com/source/building-devices.html  (alternatively, you can use my flash.sh script), or run the emulator (my script device.sh runs a basic emulated device).