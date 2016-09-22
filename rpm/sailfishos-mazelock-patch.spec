Name:       sailfishos-mazelock-patch

BuildArch: noarch

Summary:    MazeLock patch for Devicelock
Version:    0.2.0
Release:    1
Group:      Qt/Qt
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-version >= 2.0.4

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
mkdir -p %{buildroot}/usr/lib/qt5/qml/com/jolla/settings/system
cp -r qml/*.qml %{buildroot}/usr/lib/qt5/qml/com/jolla/settings/system/

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
%{_libdir}/qt5/qml/com/jolla/settings/system