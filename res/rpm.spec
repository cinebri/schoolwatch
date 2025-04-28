Name:       schoolwatch
Version:    1.3.9
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://schoolwatch.com
Vendor:     schoolwatch <info@schoolwatch.com>
Requires:   gtk3 libxcb libxdo libXfixes alsa-lib libva2 pam gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/schoolwatch/
mkdir -p %{buildroot}/usr/share/schoolwatch/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/schoolwatch %{buildroot}/usr/bin/schoolwatch
install $HBB/libsciter-gtk.so %{buildroot}/usr/share/schoolwatch/libsciter-gtk.so
install $HBB/res/schoolwatch.service %{buildroot}/usr/share/schoolwatch/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/schoolwatch.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/schoolwatch.svg
install $HBB/res/schoolwatch.desktop %{buildroot}/usr/share/schoolwatch/files/
install $HBB/res/schoolwatch-link.desktop %{buildroot}/usr/share/schoolwatch/files/

%files
/usr/bin/schoolwatch
/usr/share/schoolwatch/libsciter-gtk.so
/usr/share/schoolwatch/files/schoolwatch.service
/usr/share/icons/hicolor/256x256/apps/schoolwatch.png
/usr/share/icons/hicolor/scalable/apps/schoolwatch.svg
/usr/share/schoolwatch/files/schoolwatch.desktop
/usr/share/schoolwatch/files/schoolwatch-link.desktop
/usr/share/schoolwatch/files/__pycache__/*

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
    rm /usr/share/applications/schoolwatch.desktop || true
    rm /usr/share/applications/schoolwatch-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
