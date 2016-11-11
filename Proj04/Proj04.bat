echo off

rem set the path
path=%path%;"C:\Users\Velislav\Desktop\batfile\Proj04\Proj04Runner.txt"

rem perform the test
python -m doctest Proj04Runner.txt

pause