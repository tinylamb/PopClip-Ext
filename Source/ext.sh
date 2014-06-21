#!/bin/zsh

help()
{
cat << HELP
ext
    -- build Popclip extention from source file
USAGE:
    ./ext [-h] source_file_name
OPTIONS:
    -h help text
EXAMPLE: 
    ./ext DoubanDiary
HELP
exit 0
}
if [ $# -eq 0 ] || [ $1 = "-h" ]; then
    help
else
    cp -r $1 ../Downloads/$1.popclipext
    zip -r ../Downloads/$1.popclipextz $1
fi
