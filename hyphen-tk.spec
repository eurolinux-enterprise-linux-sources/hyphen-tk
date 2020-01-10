Name: hyphen-tk
Summary: Turkmen hyphenation rules
%define upstreamid 20110620
Version: 0.%{upstreamid}
Release: 4%{?dist}
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-tk.tex?view=co
Source: hyph-tk.tex
Group: Applications/Text
URL: http://tug.org/tex-hyphen
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: Public Domain
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-tk-cleantex.patch

%description
Turkmen hyphenation rules.

%prep
%setup -T -q -c -n hyphen-tk
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-tk.tex hyph_tk_TM.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 15 hyph-tk.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_tk_TM.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/hyph_tk_TM.dic

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110620-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110620-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110620-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110620-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100531-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100531-1
- latest version

* Sat Apr 03 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100319-1
- latest version

* Tue Mar 16 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100315-1
- initial version
