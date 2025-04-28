Name:       schoolwatch
Version:    1.3.9
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://schoolwatch.com
Vendor:     schoolwatch <info@schoolwatch.com>
Requires:   gtk3 libxcb1 xdotool libXfixes3 alsa-utils libXtst6 libva2 pam gstreamer-plugins-base gstreamer-plugin-pipewire
Recommends: libayatana-appindicator3-1
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libfile_selector_linux_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit), libtexture_rgba_renderer_plugin.so()(64bit)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/share/schoolwatch" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/share/schoolwatch"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/schoolwatch.service -t "%{buildroot}/usr/share/schoolwatch/files"
install -Dm 644 $HBB/res/schoolwatch.desktop -t "%{buildroot}/usr/share/schoolwatch/files"
install -Dm 644 $HBB/res/schoolwatch-link.desktop -t "%{buildroot}/usr/share/schoolwatch/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/schoolwatch.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/schoolwatch.svg"

%files
/usr/share/schoolwatch/*
/usr/share/schoolwatch/files/schoolwatch.service
/usr/share/icons/hicolor/256x256/apps/schoolwatch.png
/usr/share/icons/hicolor/scalable/apps/schoolwatch.svg
/usr/share/schoolwatch/files/schoolwatch.desktop
/usr/share/schoolwatch/files/schoolwatch-link.desktop

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop schoolwatch || true
  ;;
esac

%post
cp /usr/share/schoolwatch/files/schoolwatch.service /etc/systemd/system/schoolwatch.service
cp /usr/share/schoolwatch/files/schoolwatch.desktop /usr/share/applications/
cp /usr/share/schoolwatch/files/schoolwatch-link.desktop /usr/share/applications/
ln -sf /usr/share/schoolwatch/schoolwatch /usr/bin/schoolwatch
systemctl daemon-reload
systemctl enable schoolwatch
systemctl start schoolwatch
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop schoolwatch || true
    systemctl disable schoolwatch || true
    rm /etc/systemd/system/schoolwatch.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/bin/schoolwatch || true
    rmdir /usr/lib/schoolwatch || true
    rmdir /usr/local/schoolwatch || true
    rmdir /usr/share/schoolwatch || true
    rm /usr/share/applications/schoolwatch.desktop || true
    rm /usr/share/applications/schoolwatch-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
    rmdir /usr/lib/schoolwatch || true
    rmdir /usr/local/schoolwatch || true
  ;;
esac
