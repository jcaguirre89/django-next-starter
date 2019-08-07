import React from 'react';
import Link from 'next/link';

export default function About() {
  return (
    <div>
      <p>My name is Cristobal</p>
      <Link href="/">
        <a>Home</a>
      </Link>
    </div>
  );
}
