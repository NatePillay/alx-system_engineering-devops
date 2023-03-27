# install a package
package { 
  'flash':
  ensure => '2.1.0',
  provider => 'pip3',
}
