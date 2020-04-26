shopt -s extdebug


preexec_invoke_exec () {
    [ -n "$COMP_LINE" ] && return  # do nothing if completing
    [ "$BASH_COMMAND" = "$PROMPT_COMMAND" ] && return # don't cause a preexec for $PROMPT_COMMAND
    #echo "=------------------"
    #history 1
    local orig=`HISTTIMEFORMAT= history 1 | sed -e "s/^[ ]*[0-9]*[ ]*//"`;

	# if not orig-cmdline (trim leading space) starts with hebrew (or: second char is hebrew), then
	if [[ $orig =~ ^\ *([א-ת\']|.[א-ת\']) ]] ; then

		# So that you don't get locked accidentally
		if [ "shopt -u extdebug" == "$orig" ]; then  return 0 ;  fi

		# Modify $orig and then execute it
		cmd=`heb2eng.py $orig`
		$cmd
		return 1 # This prevent executing of original command
	fi
}
trap 'preexec_invoke_exec' DEBUG
