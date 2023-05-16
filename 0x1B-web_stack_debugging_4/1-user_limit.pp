#login as holberton and open any number of files without error messages
exec {'open files no lim':
	command => 'sed -rie \'s/(holberton (hard|soft) nofile).*/\1 1000/gi\'/etc/security/limits.conf',
	path => 'usr/bin/:/bin/'
}
