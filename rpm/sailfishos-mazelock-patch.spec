Name:       sailfishos-mazelock-patch

BuildArch: noarch

Summary:    MazeLock patch for Devicelock
Version:    0.1.3
Release:    1
Group:      Qt/Qt
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-version >= 1.1.9
Requires:   lipstick-jolla-home-qt5 >= 0.28.7.34

%description
MazeLock patch for Devicelock

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-mazelock-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-mazelock-patch
mkdir -p %{buildroot}/usr/share/jolla-settings/pages/sailfishos-mazelock-patch
cp -r settings/*.qml %{buildroot}/usr/share/jolla-settings/pages/sailfishos-mazelock-patch
cp -r settings/*.png %{buildroot}/usr/share/jolla-settings/pages/sailfishos-mazelock-patch
mkdir -p %{buildroot}/usr/share/jolla-settings/entries
cp -r settings/*.json %{buildroot}/usr/share/jolla-settings/entries/

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-mazelock-patch ]; then
/usr/sbin/patchmanager -u sailfishos-mazelock-patch || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-mazelock-patch ]; then
/usr/sbin/patchmanager -u sailfishos-mazelock-patch || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-mazelock-patch
%{_datadir}/jolla-settings/entries
%{_datadir}/jolla-settings/pages