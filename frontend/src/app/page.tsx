import { Suspense } from "react";
import SalesPage from "./sales/page";

export default function Home() {
  return (
    <Suspense fallback={<p className="text-center">Loading Sales Page...</p>}>
      <SalesPage />
    </Suspense>
  );
}