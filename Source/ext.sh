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

ext(){
    local source_dir=$(pwd)
    local ext_dir=../Downloads
    [ -e $ext_dir/"$1".popclipext ] && rm -fr $ext_dir/"$1".*
    cp -r "$source_dir"/"$1" $ext_dir/"$1".popclipext
    zip -r $ext_dir/"$1".popclipextz $ext_dir/"$1".popclipext
}

if [ $# -eq 0 ] || [ "$1" = "-h" ]; then
    help
else
    ext "$1"
    #rm -fr ../Downloads/$1.*
    #cp -r $1 ../Downloads/$1.popclipext
    #zip -r ../Downloads/$1.popclipextz ../Downloads/$1.popclipext
fi
