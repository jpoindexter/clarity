import Image from "next/image";

export default function Home() {
  return (
    <div>
      <main style={{ textAlign: "center", padding: "20px" }}>
        <Image
          src="/next.svg"
          alt="Next.js logo"
          width={180}
          height={38}
          priority
        />
        <ol style={{ listStyleType: "none", padding: 0 }}>
          <li>
            Get started by editing <code>src/app/page.tsx</code>.
          </li>
          <li>Save and see your changes instantly.</li>
        </ol>

        <div>
          <a
            style={{
              display: "inline-block",
              padding: "10px 20px",
              margin: "10px",
              backgroundColor: "#0070f3",
              color: "#ffffff",
              textDecoration: "none",
              borderRadius: "5px",
            }}
            href="https://vercel.com/new?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Image
              src="/vercel.svg"
              alt="Vercel logomark"
              width={20}
              height={20}
            />
            Deploy now
          </a>
          <a
            href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              display: "inline-block",
              padding: "10px 20px",
              margin: "10px",
              backgroundColor: "#eaeaea",
              textDecoration: "none",
              borderRadius: "5px",
            }}
          >
            Read our docs
          </a>
        </div>
      </main>
      <footer style={{ textAlign: "center", padding: "20px" }}>
        <a
          href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
          style={{ margin: "10px" }}
        >
          <Image src="/file.svg" alt="File icon" width={16} height={16} />
          Learn
        </a>
        <a
          href="https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
          style={{ margin: "10px" }}
        >
          <Image src="/window.svg" alt="Window icon" width={16} height={16} />
          Examples
        </a>
        <a
          href="https://nextjs.org?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
          style={{ margin: "10px" }}
        >
          <Image src="/globe.svg" alt="Globe icon" width={16} height={16} />
          Go to nextjs.org →
        </a>
      </footer>
    </div>
  );
}
