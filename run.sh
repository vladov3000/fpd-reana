rm -r workdir
WORKFLOW=${1:-ma5.yml}
yadage-run workdir $WORKFLOW inputs/input.yml -d initdir=$PWD/inputs

