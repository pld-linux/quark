Summary:	Quark is an audio player, for geeks, by geeks
Name:		quark
Version:	3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://quark.nerdnest.org/%{name}-%{version}.tar.gz
# Source0-md5:	cef037af5cd0fff762496cc930c2fdb9
BuildRequires:	xine-lib-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	GConf2-devel
BuildRequires:	gnome-vfs2-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quark is an audio player, for geeks, by geeks. It runs in the
background with access provided via a FIFO in the filesystem. It uses
Xine-lib for playing music, and can therefore play any file format
supported by Xine.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install schemas in proper location
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas
install quark/quark.schemas $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas
install strange-quark/strange-quark.schemas $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

%find_lang %{name}

%post
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/charm-quark
%attr(755,root,root) %{_bindir}/quark
%attr(755,root,root) %{_bindir}/strange-quark
%{_sysconfdir}/gconf/schemas/*.schemas
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
