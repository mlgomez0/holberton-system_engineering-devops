#set up your client SSH configuration file
class { 'ssh':
  storeconfigs_enabled => false,
  server_options       => {
    'Match User www-data' => {
      'PasswordAuthentication' => 'no',
      'IdentityFile'           => '~/.ssh/holberton'
    },
  },
}
