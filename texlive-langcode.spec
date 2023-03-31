Name:		texlive-langcode
Version:	27764
Release:	2
Summary:	TeXLive langcode package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive langcode package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/langcode/langcode.sty
%doc %{_texmfdistdir}/doc/generic/langcode/README
%doc %{_texmfdistdir}/doc/generic/langcode/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/generic/langcode/langcode.pdf
#- source
%doc %{_texmfdistdir}/source/generic/langcode/langcode.tex
%doc %{_texmfdistdir}/source/generic/langcode/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
