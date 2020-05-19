#correct spelling error in word press settings file
exec {'debugApache-WP':
  provider => shell,
  command  => 'sudo sed -i "s+define('WP_DEBUG', false);+define('WP_DEBUG', true);" /var/www/html/wp-config.php && sudo sed -i "s+require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );+require_once( ABSPATH . WPINC . '/class-wp-locale.php' );" /var/www/html/wp-settings.php',
}
