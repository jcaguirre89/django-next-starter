import Link from 'next/link';

function Home() {
  return (
    <div>
      <h2>Hello!</h2>
      <Link href="/about">
        <a>About</a>
      </Link>
    </div>
  );
}

export default Home;
