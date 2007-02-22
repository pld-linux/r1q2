Summary:	R1CHs Enhanced Quake II Client/Server
Name:		r1q2
Version:	7187
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.r1ch.net/stuff/r1q2/src/%{name}-b%{version}-src.zip
# Source0-md5:	66669adc5a114387e3eb6c3baa661ec2
URL:		http://www.r1ch.net/stuff/r1q2/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
R1Q2 is an enhanced client/server for Quake II. Based on the id
Software 3.21 source, rather than concentrate on fancy graphics,
embedded MP3 players and other "gimmick" features, R1Q2 is focused on
providing stability, security and speed whilst remaining fully
compatible with existing mods and other clients.

%prep
%setup -qc

%build
%{__make} -C binaries \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog readme.txt
