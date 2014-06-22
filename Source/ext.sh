#!/bin/zsh

#why script failed but manual success
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
    cp -r $1 ../Downloads/$1
    cd ../Downloads
    mv $1 $1.popclipext
    zip -r $1.popclipext.zip $1.popclipext
    mv $1.popclipext.zip $1.popclipextz
fi
