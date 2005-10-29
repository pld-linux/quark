Summary:	quark is an audio player, for geeks, by geeks
Summary(pl):	quark to odtwarzacz d¼wiêku pisany przez geeków dla geeków
Name:		quark
Version:	3.21
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://quark.sunsite.dk/%{name}-%{version}.tar.gz
# Source0-md5:	d2e16ef97b9107df27ac4a8ba269b6ab
Patch0:		%{name}-desktop.patch
URL:		http://quark.sunsite.dk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel
Requires(post,preun):	GConf2
Requires:	xine-plugin-audio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
quark is an audio player, for geeks, by geeks. It runs in the
background with access provided via a FIFO in the filesystem. It uses
Xine-lib for playing music, and can therefore play any file format
supported by Xine.

%description -l pl
quark to odtwarzacz d¼wiêku pisany przez geeków dla geeków. Dzia³a w
tle z dostêpem przez nazwany potok umieszczony w systemie plików. Do
odtwarzania muzyki u¿ywa Xine-lib, wiêc mo¿e odtwarzaæ pliki w
dowolnym formacie obs³ugiwanym przez Xine.

%package charm
Summary:	CLI for quark
Summary(pl):	CLI dla quarka
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description charm
Simple bash script to controlling quark via command line.

%description charm -l pl
Prosty skrypt basha do sterowania quarkiem z linii poleceñ.

%package strange
Summary:	GUI for quark
Summary(pl):	GUI dla quarka
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description strange
Based on gtk+2 GUI for quark.

%description strange -l pl
Oparte na gtk+2 GUI dla quarka.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--enable-debug=%{?debug:yes}%{!?debug:no}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
%gconf_schema_install quark.schemas

%postun
%gconf_schema_uninstall quark.schemas

%post strange
%gconf_schema_install strange-quark.schemas

%postun strange
%gconf_schema_uninstall strange-quark.schemas

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/quark
%{_sysconfdir}/gconf/schemas/quark.schemas

%files charm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/charm-quark

%files strange
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/strange-quark
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_sysconfdir}/gconf/schemas/strange-quark.schemas
