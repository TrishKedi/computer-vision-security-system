"use client"

import { useEffect, useState } from "react"
import axios from "axios"

type Detection = {
  label: string
  confidence: number
  timestamp: string
  image: string
}

export default function Home() {
  const [detections, setDetections] = useState<Detection[]>([])

  const BASE_URL = process.env.NEXT_PUBLIC_BASE_URL

  useEffect(() => {
    axios.get(`${BASE_URL}/detections`).then((res) => {
      setDetections(res.data.reverse()) // newest first
    })
  }, [])

  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">AI Security Detections</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {detections.map((d, idx) => (
          <div key={idx} className="border p-4 rounded shadow">
            <img
              src={`${BASE_URL}/image/${d.image}`}
              alt={`Detection ${idx}`}
              className="w-full h-auto mb-2"
            />
            <p><strong>Label:</strong> {d.label}</p>
            <p><strong>Confidence:</strong> {d.confidence}</p>
            <p><strong>Time:</strong> {d.timestamp}</p>
          </div>
        ))}
      </div>
    </main>
  )
}
