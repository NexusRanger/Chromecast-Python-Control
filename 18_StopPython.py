# Kill all processes with the name "python.exe" (If it's hung up)

import subprocess

subprocess.run(['taskkill', '/f', '/im', 'python.exe'])

# (May need to kill the Visual Studio Code terminal first - with bin icon in terminal)