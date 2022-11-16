Name:		texlive-texnegar
Version:	57692
Release:	1
Summary:	Kashida justification in XeLaTeX and LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texnegar
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texnegar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texnegar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texnegar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In some cursive scripts such as Persian or Arabic, kashida is
used to create justification. In this type of justification
characters are elongated rather than expanding spaces between
words. The kashida justification in xepersian has many bugs.
Also it has problems with some fonts. The xepersian-hm package
was the first attempt to fix these bugs in xepersian, which
uses the XeTeX engine. This package extends the kashida
justification to be used with the LuaTeX engine, too.
Explanation of the package name: Negar, in Persian, is the
present stem of negaashtan meaning to design, to paint, to
write; and as a noun it means "sweetheart, idol, beloved,
figuratively referring to a beautiful woman, pattern, painting,
and artistic design".

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/texnegar
%{_texmfdistdir}/tex/latex/texnegar
%doc %{_texmfdistdir}/doc/latex/texnegar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
