on run {daemon_file, agent_file, user}

  set sh1 to "echo " & quoted form of daemon_file & " > /Library/LaunchDaemons/com.carriez.SchoolWatch_service.plist && chown root:wheel /Library/LaunchDaemons/com.carriez.SchoolWatch_service.plist;"

  set sh2 to "echo " & quoted form of agent_file & " > /Library/LaunchAgents/com.carriez.SchoolWatch_server.plist && chown root:wheel /Library/LaunchAgents/com.carriez.SchoolWatch_server.plist;"

  set sh3 to "cp -rf /Users/" & user & "/Library/Preferences/com.carriez.SchoolWatch/SchoolWatch.toml /var/root/Library/Preferences/com.carriez.SchoolWatch/;"

  set sh4 to "cp -rf /Users/" & user & "/Library/Preferences/com.carriez.SchoolWatch/SchoolWatch2.toml /var/root/Library/Preferences/com.carriez.SchoolWatch/;"

  set sh5 to "launchctl load -w /Library/LaunchDaemons/com.carriez.SchoolWatch_service.plist;"

  set sh to sh1 & sh2 & sh3 & sh4 & sh5

  do shell script sh with prompt "SchoolWatch want to install daemon and agent" with administrator privileges
end run
