set -o errexit
set -o nounset

main() {

  # $# -> number of params
  # exit 1 -> indicates error
  # http://tldp.org/LDP/abs/html/exitcodes.html 

  if [ "$#" -ne 1 ]; then
    echo "Usage: ./error_handling <greetee>"
    exit 1
  fi

  echo "Hello, ${1-World}"
}

main "$@"
