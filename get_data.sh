#!/bin/sh
[ -z "$1" ] && echo "Usage:  $0 <filename>" && exit 1
[ ! -f "$1" ] && nc 142.132.30.73 4210 | pv > $1
exit 0
