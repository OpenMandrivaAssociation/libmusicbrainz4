#!/bin/sh
# This is a compat package -- skip versions newer than 4.x
git ls-remote --tags https://github.com/metabrainz/libmusicbrainz 2>/dev/null|awk '{ print $2; }' |grep -v '\^{}' |sed -e 's,refs/tags/,,;s,_,.,g' |sed -e 's,^v,,' |grep '^release-4' |sed -e 's,^release-,,' |sort -V |tail -n1
