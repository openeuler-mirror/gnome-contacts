Name:           gnome-contacts
Version:        3.30.1
Release:        2
Summary:        Integrated address book for GNOME
License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Contacts
Source0:        https://download.gnome.org/sources/gnome-contacts/3.30/gnome-contacts-%{version}.tar.xz
BuildRequires:  desktop-file-utils docbook-dtds docbook-style-xsl gettext meson vala libappstream-glib
BuildRequires:  libxslt pkgconfig(cheese-gtk) pkgconfig(folks) >= 0.11.4 pkgconfig(folks-eds)
BuildRequires:  pkgconfig(folks-telepathy) pkgconfig(gee-0.8) pkgconfig(gnome-desktop-3.0) pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) pkgconfig(gtk+-3.0) >= 3.22.0
Requires:       folks >= 1:0.11.4 gtk3 >= 3.22.0 hicolor-icon-theme

%description
Contacts is GNOME's integrated address book. It is written in Vala and uses libfolks
(also written in Vala) and Evolution Data Server.

%package        help
Summary:        Documentation for gnome-contacts
BuildArch:      noarch
Requires:       gnome-contacts = %{version}-%{release}

%description    help
Documentation for gnome-contacts.

%prep
%autosetup -n gnome-contacts-%{version}
%build
%meson
%meson_build
%install
%meson_install
%find_lang gnome-contacts
%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Contacts.desktop

%files -f gnome-contacts.lang
%doc AUTHORS NEWS COPYING
%{_bindir}/gnome-contacts
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/{org.gnome.Contacts.service,org.gnome.Contacts.SearchProvider.service}
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Contacts.png
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Contacts-symbolic.svg
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml

%files help
%{_mandir}/man1/gnome-contacts.1*

%changelog
* Wed Dec 11 2019 Ling Yang <lingyang2@huawei.com> - 3.30.1-2
- Package init
