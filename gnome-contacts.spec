%global gtk4_version 4.6

Name:           gnome-contacts
Version:        42.0
Release:        1
Summary:        Integrated address book for GNOME
License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Contacts
Source0:        https://download.gnome.org/sources/%{name}/42/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils docbook-dtds docbook-style-xsl gettext meson vala libappstream-glib
BuildRequires:  libxslt pkgconfig(folks) >= 0.11.4 pkgconfig(folks-eds)
BuildRequires:  pkgconfig(folks-telepathy) pkgconfig(gee-0.8) pkgconfig(goa-1.0) pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0) pkgconfig(libportal)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}

Requires:       folks >= 1:0.11.4 gtk4%{?_isa} >= %{gtk4_version} hicolor-icon-theme

%description
Contacts is GNOME's integrated address book. It is written in Vala and uses libfolks
(also written in Vala) and Evolution Data Server.

%package_help

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Contacts.desktop

%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-contacts
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Contacts*.svg
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml

%files help
%doc NEWS
%{_mandir}/man1/gnome-contacts.1*

%changelog
* Mon Mar 28 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 42.0-1
- Update to 42.0

* Wed Jun 16 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.1-1
- Upgrade to 3.38.1

* Wed Dec 11 2019 Ling Yang <lingyang2@huawei.com> - 3.30.1-2
- Package init
