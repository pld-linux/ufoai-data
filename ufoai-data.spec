%define	_name	ufoai
Summary:	"UFO: Alien Invasion" - squad-based tactical strategy game in the tradition of the old X-COM PC games
Summary(pl.UTF-8):	"UFO: Alien Invasion" - gra strategiczna utrzymana w tradycji starych gier X-COM z PC
Name:		ufoai-data
Version:	2.3
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://downloads.sourceforge.net/ufoai/%{version}/data.tar
# Source0-md5:	08fa6d5c80231468c4d5e886600c8dcf
URL:		http://ufoai.sourceforge.net/
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

This package contains "UFO: Alien Invasion" data files.

%description -l pl.UTF-8
Jest rok 2084. Kierujesz tajną organizacją, która ma obronić Ziemię
przed brutalnymi wrogami. Buduj swoje bazy, przygotuj swój zespół i
wpadnij w wir szybkiej turowej walki.

"UFO: Alien Invasion" to oparta o oddziały gra strategiczna utrzymana
w tradycji starych gier X-COM z PC, ale z pewnymi zmianami. Gra łączy
realizm militarny z ciężkim science-fiction i dziwnością inwacji
wroga. Uważnie skonstruowany system turowy daje kontrolę nad oddziałem
zachowując poczucie kroku i niebezpieczeństwa.

W ciągu długiego czasu gracz musi prowadzić badania narażając się
wrogom, aby odkryć ich tajemnicze cele i użyć ich potężnych broni dla
własnych potrzeb. Gracz wytworzy unikalne przedmioty i wykorzysta je w
walce przeciwko swoim wrogom. Można także używać ich przeciwko
przyjaciołom w przypadku gry dla wielu graczy.

Ten pakiet zawiera pliki danych gry "UFO: Alien Invasion".

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
