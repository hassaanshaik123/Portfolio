import type { Metadata } from "next";
import { Providers } from "@/components/providers";
import { Navbar } from "@/components/navbar";
import { ScrollProgress } from "@/components/motion";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "Muhammad Hassaan | Sales & Business Developer",
    template: "%s | Muhammad Hassaan",
  },
  description:
    "Explore Muhammad Hassaan’s work in consultative sales, community growth, business development and product experiments.",
  icons: { icon: "/assets/h-logo.png" },
};
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <Providers>
          <a className="skip-link" href="#main">
            Skip to content
          </a>
          <ScrollProgress />
          <Navbar />
          {children}
        </Providers>
        <noscript>
          <style>{`.reveal-motion{opacity:1!important;transform:none!important}.opening-overlay{display:none!important}`}</style>
        </noscript>
      </body>
    </html>
  );
}
