ARG PHP_VERSION=7.3

FROM egordm/wde:php$PHP_VERSION

# Install Experius Magento tools
ARG DEV_USER=magnetron
ARG DB_HOST=172.18.18.200
ARG DB_USER=magnetron
ARG DB_PASSWORD=magnetron
ARG MAGENTO_USERNAME=magnetron
ARG MAGENTO_PASSWORD=Magnetr0n!
ARG MAGENTO_USER_EMAIL=magnetron@example.com
ARG MAGENTO_ADMIN_URL=admin
ARG MAGENTO_MODULE_VENDOR=Magnetron
ARG GIT_REPO_VENDOR=magnetron
ARG MAGENTO_MARKETPLACE_USER=""
ARG MAGENTO_MARKETPLACE_PASS=""
ARG DOMAIN_SUFFIX=dev

ADD container/install_magento_tools.sh $DEV_TOOLS/install_magento_tools.sh
RUN bash $DEV_TOOLS/install_magento_tools.sh

# Install dev tools
RUN cd ~/tools && \
    curl -O https://files.magerun.net/n98-magerun2.phar && \
    curl -O https://files.magerun.net/n98-magerun.phar && \
    ln -s ~/tools/n98-magerun2.phar ~/tools/magerun2 && \
    ln -s ~/tools/n98-magerun.phar ~/tools/magerun && \
    chmod 0777 ~/tools/* && \
    printf "export PATH=\$PATH:~/tools\n" >> ~/.bashrc && \
    cd ~

# RUN sudo pip install mage2gen