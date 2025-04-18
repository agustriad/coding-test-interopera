"use client";
import { useEffect } from "react";
import useSalesStore from "../../store/salesStore";
import CardSales from "@/components/CardSales";

export default function SalesPage() {
  const { salesReps, loading, fetchSales } = useSalesStore();

  useEffect(() => {
    fetchSales();
  }, [fetchSales]);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-gray-900"></div>
      </div>
    );
  }

  return (
    <div>
      <div className="p-8">
        <h1 className="text-2xl font-bold mb-6">List Sales</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {salesReps.map((rep, index) => (
            <div key={rep.id || index} className="p-4 border rounded-lg shadow-md">
              <CardSales name={rep.name} clients={rep.clients} region={rep.region} role={rep.role} skills={rep.skills} id={rep.id || index}/>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}