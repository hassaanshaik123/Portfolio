import type { NextConfig } from "next";
const nextConfig: NextConfig = {
  async redirects() {
    return [
      { source: "/index.html", destination: "/", permanent: true },
      { source: "/projects.html", destination: "/projects", permanent: true },
    ];
  },
};
export default nextConfig;
