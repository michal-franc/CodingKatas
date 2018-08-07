#!/usr/bin/bash

# ${#1} returns the len of the first argument

main() {
  if [ "${#1}" = 0 ]; then
    echo ""
  fi

  res=""

  for (( i = ${#1} -1; i >= 0; i--)); do
    res="$res${1:$i:1}"
  done

  echo $res
}

main "$@"
