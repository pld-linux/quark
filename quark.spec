Summary:	quark is an audio player, for geeks, by geeks
Summary(pl):	quark to odtwarzacz d¼wiêku pisany przez geeków dla geeków
Name:		quark
Version:	3.21
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://quark.nerdnest.org/%{name}-%{version}.tar.gz
# Source0-md5:	d2e16ef97b9107df27ac4a8ba269b6ab
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	xine-lib-devel
Requires(post):	GConf2
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
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
%attr(755,root,root) %{_bindir}/quark
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_sysconfdir}/gconf/schemas/*.schemas

%files charm
%attr(755,root,root) %{_bindir}/charm-quark

%files strange
%attr(755,root,root) %{_bindir}/strange-quark
