%global gtk4_version 4.6

Name:           gnome-contacts
Version:        43.0
Release:        1
Summary:        Contacts manager for GNOME
License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Contacts
Source0:        https://download.gnome.org/sources/%{name}/43/%{name}-%{version}.tar.xz

Patch0:         213.patch
Patch1:         214.patch
Patch2:         216.patch

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  libappstream-glib
BuildRequires:  libxslt
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(folks-eds)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal-gtk4)

Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       hicolor-icon-theme

%description
%{name} is a standalone contacts manager for GNOME desktop.

%package_help

%prep
%autosetup -p1 -n %{name}-%{version}

%build
export VALAFLAGS="-g"
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
%{_libexecdir}/gnome-contacts/
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Contacts*.svg
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml

%files help
%doc NEWS
%{_mandir}/man1/gnome-contacts.1*

%changelog
* Mon Jan 02 2023 lin zhang <lin.zhang@turbolinux.com.cn> - 43.0-1
- Update to 43.0

* Mon Mar 28 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 42.0-1
- Update to 42.0

* Wed Jun 16 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.1-1
- Upgrade to 3.38.1

* Wed Dec 11 2019 Ling Yang <lingyang2@huawei.com> - 3.30.1-2
- Package init
