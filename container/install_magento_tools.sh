#!/bin/sh

mkdir ~/tools

# Setup magento login
{
  printf "
{
    \"http-basic\": {
        \"repo.magento.com\": {
            \"username\": \"${MAGENTO_MARKETPLACE_USER}\",
            \"password\": \"${MAGENTO_MARKETPLACE_PASS}\"
        }
    }
}
"
} >  ~/.composer/auth.json

# Install coding standard
composer create-project --repository=https://repo.magento.com magento/marketplace-eqp ~/tools/magento-coding-standard

# Install experius magneto tools
MAGETOOLS_PATH=~/tools/Magento-2-Bash-Localhost-Installation-Script
git clone https://github.com/EgorDm/Magento-2-Bash-Localhost-Installation-Script.git $MAGETOOLS_PATH

# Update config
CONFIG_PATH=$MAGETOOLS_PATH/config.sh
cp $MAGETOOLS_PATH/config.sample.sh $CONFIG_PATH

# shellcheck disable=SC2112
function change_config() {
    sed "s/^$1=.*/$1=$2/g" -i $CONFIG_PATH
}

change_config MYSQL_HOST \"\${DB_HOST}\"
change_config MYSQL_USER \"\${DB_USER}\"
change_config MYSQL_PASSWORD \"\${DB_PASSWORD}\"

change_config MAGENTO_USERNAME \"\${MAGENTO_USERNAME}\"
change_config MAGENTO_PASSWORD \"\${MAGENTO_PASSWORD}\"
change_config MAGENTO_USER_EMAIL \"\${MAGENTO_USER_EMAIL}\"
change_config MAGENTO_ADMIN_URL \"\${MAGENTO_ADMIN_URL}\"
change_config MAGENTO_MODULE_VENDOR \"\${MAGENTO_MODULE_VENDOR}\"

change_config GIT_REPO_VENDOR \"\${GIT_REPO_VENDOR}\"

change_config DOMAIN_PREFIX \"\"
change_config DOMAIN_SUFFIX \".dev\"
change_config FOLDER_SUFFIX \"\"

change_config PHP7 \"php$PHP_VERSION\"

change_config secure \"true\"

# Update bash
{
  printf "export PATH=\$PATH:$MAGETOOLS_PATH\n"
  printf "if [ -f $MAGETOOLS_PATH/.bash_xp ]; then
      . $MAGETOOLS_PATH/.bash_xp
  fi
  "
} >> ~/.bashrc