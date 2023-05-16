#we simulated a number of http requests to the server and have recieved errors regarding the number of simulations
exec {'webstack-debug':
	command => '/bin/sed -i "s/15/1000/" /etc/default/nginx'
}

exec {'nginx':
	require => Exec['webstack-debug'],
	command => '/usr/sbin/service nginx restart'
}
