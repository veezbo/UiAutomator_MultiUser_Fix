Multi-User UiAutomator Fix
=========================

    UPDATED 9/4/13

Fixes the problem UiAutomator currently has with multiple users in the Android Open Source Project.

The prior fix that relied on the uiautomator_fix.py script is no longer necessary. It is recommended to avoid using this method entirely (as it may have side effects), but the instructions for doing so are included at the end of this README.

The current fix identifies the problem, and fixes that problem directly in a way that will not have side effects on other applications.

For more information, see the [bug report] [1]
and the [AOSP patch] [2] I submitted (currently in the reviewing process).

  [1]: http://code.google.com/p/android/issues/detail?id=58987 "Bug Report"
  [2]: https://android-review.googlesource.com/64730 "AOSP Patch"

Instructions
------------

In the repo, I've included my locally-built uiautomator.jar files with the fix applied (built for generic, maguro, and manta). Pick the one you need and see if it works for you. Also, I think you'll want to rename the .jar file back to uiautomator.jar before doing anything with it.

Otherwise, follow these steps for downloading and applying the fix to AOSP:

1. Initialize your [environment] [1]. 
2. Download the [source] [2]. I would recommend running repo sync -j#, where # is at least the number of cores you have on your computer.
3. You'll then want to modify the Launcher.java file as I have in the bug fix.
4. Then, you'll need to [build it] [3]. Alternatively, you can use the script under my Android_Scripts repo called build.sh.
5. Finally, you need to [flash your device] [4] or [run the emulator] [5]. You can also just use my device.sh or emulator.sh scripts.

  [1]: http://source.android.com/source/initializing.html "environment"
  [2]: http://source.android.com/source/downloading.html#initializing-a-repo-client "source"
  [3]: http://source.android.com/source/building-running.html "building"
  [4]: http://source.android.com/source/building-devices.html "flash_device"
  [5]: http://developer.android.com/tools/help/emulator.html#startup-options "run_emulator"  


### Using the prior fix with uiautomator_fix.py (NOT RECOMMENDED)

Support for changing the necessary file in the SDK's is included, but it is uncertain whether it is even possible to rebuild the SDK with modifications (as is necessary).

#### Instructions

1. Place the script in your AOSP directory.
2. Install Python if you don't have it, and install the pyparsing library as well (recommended: using pip).
3. Run the script, and follow the prompts.
4. Rebuild AOSP (I've provided build scripts in my Android_Scripts repo, which you can use as you desire)
5. Now, uiautomator should have multi-user support on both devices and emulators built or flashed from AOSP.

#### WARNING

Please be aware that this is not an official solution. Furthermore, this is a workaround that directly modifies internal AOSP code. It is highly recommended (and you will be given a prompt to do so) that you backup the file that is modified, so that you can replace it after you've finished using UiAutomator.