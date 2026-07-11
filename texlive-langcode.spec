%global tl_name langcode
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Simple language-dependent settings based on language codes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/langcode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/langcode.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a command \uselangcode{<code>} to adjust language-
dependent settings such as key words, typographical conventions and
language codes (ISO 639-1). The package provides a means of selecting
macros according to the specified code, for preparing a document that is
to be separately typeset in different languages. The package is
dependent on the plainpkg package, and is already in use in the morehype
and catcodes packages.

