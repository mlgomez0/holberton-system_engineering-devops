#set up your client SSH configuration file
class { 'ssh':
  storeconfigs_enabled => false,
  client_options       => {
    'PasswordAuthentication' => 'no',
    'IdentityFile'           => '~/.ssh/holberton'
    },
}
