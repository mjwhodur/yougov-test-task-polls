# Note on building on Windows

Building the application on Windows is not a trivial task, since
many requirements are not always available out of the box.

If you are on Windows 10, you may have to install the Windows 10 SDK from https://dev.windows.com/en-us/downloads/windows-10-sdk . Otherwise, try installing KB2999226 from https://support.microsoft.com/en-us/kb/2999226. In both cases, add the
directory containing api-ms-win-crt-multibyte-l1-1-0.dll to your PATH environment variable afterwards.

Please also note, that you shall have Microsoft Visual C++ compiler installed, 
possibly using recent Microsoft Visual Studio with C++ support and CRT support.

After installing all needed requirements, setup the environment according to
[Building for Ubuntu and other Linux Distributions](building_ubuntu.md) document.

