%define	_name	ufoai
Summary:	"UFO: Alien Invasion" is a squad-based tactical strategy game in the tradition of the old X-COM PC games
Name:		ufoai-data
Version:	2.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Games/Strategy
URL:		http://ufoai.sourceforge.net/
Source0:	http://dl.sourceforge.net/ufoai/%{_name}-%{version}-data.tar
# Source0-md5:	a6bb13414d01299679c4e2effc6e41b7
Requires:	ufoai = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is the year 2084. You control a secret organisation charged with
defending Earth from a brutal alien enemy. Build up your bases,
prepare your team, and dive head-first into the fast and flowing
turn-based combat.

"UFO: Alien Invasion" is a squad-based tactical strategy game in the
tradition of the old X-COM PC games, but with a twist. This game
combines military realism with hard science-fiction and the weirdness
of an alien invasion. The carefully constructed turn-based system
gives you pin-point control of your squad while maintaining a sense of
pace and danger.

Over the long term you will need to conduct research into the alien
threat to figure out their mysterious goals and use their powerful
weapons for your own ends. You will produce unique items and use them
in combat against your enemies. If you like, you can even use them
against your friends with multiplayer functionality.

"UFO: Alien Invasion". Endless hours of gameplay -- absolutely free.

This package contains "UFO: Alien Invasion" data files.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/base
cp -rf base/*.pk3 $RPM_BUILD_ROOT%{_datadir}/%{_name}/base

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{_name}/base/*.pk3
