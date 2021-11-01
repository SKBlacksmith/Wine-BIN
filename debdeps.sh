#!/bin/bash

_debuntu_64() {
  local _as_root="sudo "; (( EUID )) || _as_root=""

  # 64-bit
  msg2 ""
  msg2 "Installing 64-bit dependencies for Debian-based distros..."
  ${_as_root}apt install git autoconf bison ccache debhelper desktop-file-utils docbook-to-man docbook-utils docbook-xsl flex fontforge gawk gettext libacl1-dev libasound2-dev libcapi20-dev libcups2-dev libdbus-1-dev libgif-dev libglu1-mesa-dev libgphoto2-dev libgsm1-dev libgtk-3-dev libkrb5-dev libxi-dev liblcms2-dev libldap2-dev libmpg123-dev libncurses5-dev libopenal-dev libosmesa6-dev libpcap-dev libpulse-dev libsane-dev libssl-dev libtiff5-dev libudev-dev libv4l-dev libva-dev libxslt1-dev libxt-dev ocl-icd-opencl-dev oss4-dev prelink sharutils unixodbc-dev valgrind schedtool libfreetype6-dev xserver-xorg-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gcc-multilib g++-multilib curl fonttools libsdl2-dev python3-tk libvulkan1 libc6-dev linux-libc-dev libkdb5-9 libppl14 libcolord2 libvulkan-dev libgnutls28-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libpng-dev libkadm5clnt-mit11 libkadm5srv-mit11 libavcodec-dev libavutil-dev libswresample-dev libavcodec58 libswresample3 libavutil56 libfaudio0 libfaudio-dev libvkd3d-dev libxinerama-dev libxcursor-dev libxrandr-dev libxcomposite-dev mingw-w64 glslang-dev glslang-tools meson wget python3-pefile rustc cargo
}

_debuntu_32() {
  local _as_root="sudo "; (( EUID )) || _as_root=""

  # 32-bit
  msg2 ""
  msg2 "Installing 32-bit dependencies for Debian-based distros..."
  ${_as_root}apt install xserver-xorg-dev:i386 libfreetype6-dev:i386 libfontconfig1-dev:i386 libglu1-mesa-dev:i386 libglu1-mesa:i386 libgl1-mesa-dev:i386 libgl1:i386 libosmesa6-dev:i386 libosmesa6:i386 mesa-common-dev:i386 libegl1-mesa-dev:i386 libegl-dev:i386 libgl-dev:i386 libglx-dev:i386 libglx0:i386 libllvm12:i386 libgles-dev:i386 libglvnd-dev:i386 libgles2-mesa-dev:i386 libvulkan-dev:i386 libvulkan1:i386 libpulse-dev:i386 libopenal-dev:i386 libncurses-dev:i386 libfaudio0:i386 libfaudio-dev:i386 libvkd3d-dev:i386 libgnutls28-dev:i386 libtiff-dev:i386 libldap-dev:i386 libcapi20-dev:i386 libpcap-dev:i386 libxml2-dev:i386 libmpg123-dev:i386 libgphoto2-dev:i386 libsane-dev:i386 libcupsimage2-dev:i386 libkrb5-dev:i386 libgsm1-dev:i386 libxslt1-dev:i386 libv4l-dev:i386 libgstreamer-plugins-base1.0-dev:i386 libudev-dev:i386 libxi-dev:i386 liblcms2-dev:i386 libibus-1.0-dev:i386 libsdl2-dev:i386 ocl-icd-opencl-dev:i386 libxinerama-dev:i386 libxcursor-dev:i386 libxrandr-dev:i386 libxcomposite-dev:i386 libavcodec58:i386 libswresample3:i386 libavutil56:i386 libgstreamer-gl1.0-0:i386 gir1.2-gst-plugins-base-1.0:i386
}
