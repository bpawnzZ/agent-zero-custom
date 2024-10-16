# Use the latest slim version of Debian
FROM --platform=$TARGETPLATFORM debian:bookworm-slim

# Set ARG for platform-specific commands
ARG TARGETPLATFORM

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    nodejs \
    npm \
    openssh-server \
    sudo \
    gosu \
    && rm -rf /var/lib/apt/lists/*

# Set up SSH
RUN mkdir /var/run/sshd && \
    echo 'root:toor' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create and activate Python virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade pip in the virtual environment
RUN python3 -m pip install --upgrade pip

# Copy initial .bashrc with virtual environment activation to a temporary location
COPY .bashrc /etc/skel/.bashrc

# Copy the modified initialize script
COPY initialize.sh /usr/local/bin/initialize.sh
RUN chmod +x /usr/local/bin/initialize.sh

# Expose SSH port
EXPOSE 22

# Create entrypoint script
RUN echo '#!/bin/bash\n\
if [ ! -z "$UID" ] && [ ! -z "$GID" ]; then\n\
    groupadd -g $GID usergroup\n\
    useradd -m -u $UID -g $GID -s /bin/bash username\n\
    echo "username ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers\n\
    cp /etc/skel/.bashrc /home/username/.bashrc\n\
    chown username:usergroup /home/username/.bashrc\n\
    exec gosu username:usergroup /usr/local/bin/initialize.sh\n\
else\n\
    exec /usr/local/bin/initialize.sh\n\
fi' > /usr/local/bin/entrypoint.sh && chmod +x /usr/local/bin/entrypoint.sh

# Use the new entrypoint script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
