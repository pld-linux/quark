#
# todo:
# - should cli client link with gtk+ libraries?
# - strange-quark separate package (first, resolve first todo item)?
#
Summary:	Quark is an audio player, for geeks, by geeks
Name:		quark
Version:	3.11
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://quark.nerdnest.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-schemas.patch
# Source0-md5:	938467f152ef4815caddcbcd32ab478d
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
%patch0 -p1

%build
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
